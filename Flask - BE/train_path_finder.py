from flask import Blueprint
from database import connection
import pymysql
from flask import jsonify, request
import all_path

path_finder_api = Blueprint('path_finder_api', __name__)


@path_finder_api.route("/finder", methods=["GET"])
def finder():
    source = int(request.args.get('source'))
    destination = int(request.args.get('destination'))

    cursor, conn = connection()
    cursor.execute(
        "SELECT * FROM train_schedule  where (division_code = 'TVC' or division_code = 'MAS' or division_code = 'MDU' or division_code='PGT' or division_code = 'SA' OR division_code = 'TPJ') and st_train_id_master_id != '99140'")
    rows = cursor.fetchall()
    stationPath = []
    edgeList = []
    lookup = {}
    for record in rows:
        stationPath.append(
            (record["station_id"], record["distance_from_source"], record["arrival_time"], record["departure_time"], record["st_train_id_master_id"], record["id"], record["division_code"]))
        if record["station_id"] not in lookup:
            lookup[record["station_id"]] = record["arrival_time"]
    # print(stationPath)
    timeLookup = {}
    for idx, station in enumerate(stationPath):

        if idx + 1 < len(stationPath):
            # distance = stationPath[idx + 1][1] - stationPath[idx][1]
            # duration = (stationPath[idx+1][2] - stationPath[idx][3])
            srcDistance = stationPath[idx][1]
            destDistance = stationPath[idx + 1][1]
            srcArrivalTime = stationPath[idx][2]
            srcDepartureTime = stationPath[idx][3]
            destArrivalTime = stationPath[idx + 1][2]
            destDepartureTime = stationPath[idx + 1][3]
            destArrivalTime = stationPath[idx + 1][2]
            destDepartureTime = stationPath[idx + 1][3]
            division_code = stationPath[idx][6]

            train = stationPath[idx + 1][4]
            sourceEd = stationPath[idx][0]
            destinationEd = stationPath[idx + 1][0]
            id = stationPath[5]
            edge = (sourceEd, destinationEd)
            edgeList.append(
                (stationPath[idx][0], stationPath[idx + 1][0], 0, 0, train, srcDistance, destDistance, srcArrivalTime, srcDepartureTime, destArrivalTime, destDepartureTime, id))

            timeLookup[edge] = {
                "srcArrivalTime": srcArrivalTime, "srcDepartureTime": srcDepartureTime, "destArrivalTime": destArrivalTime, "destDepartureTime": destDepartureTime, "id": id, "division_code": division_code}

    stationDetail, totalStations = getAllStations()
    try:
        trainDetail = getAllTrains()
        finder = all_path.PathFinder(9418, edgeList)
        routePathList = finder.find_path(source, destination)
    except Exception as e:
        raise Exception(
            "Given nodes is not available in train schedule tables")

    newPathList = []
    for record in routePathList:
        dlist = []
        pathList = record[0]
        distance = record[1]
        duration = record[2]
        for idx, stationId in enumerate(pathList):
            srcArrival = None
            srcDeparture = None
            id = None
            srcArrival = lookup[stationId]
            if idx + 1 < len(pathList):
                edge = (pathList[idx], pathList[idx + 1])
                #srcArrival = timeLookup[edge]["srcArrivalTime"]
                #srcDeparture = timeLookup[edge]["srcDepartureTime"]

                destArrivalTime = int(
                    timeLookup[edge]["destArrivalTime"])
                previous = destArrivalTime
                id = timeLookup[edge]["id"]
                division_code = timeLookup[edge]["division_code"]
                print(edge, timeLookup[edge])

            trainNumber = record[3]
            stationName = stationDetail[stationId]["station_name"].strip()
            train_name = trainDetail[trainNumber].strip()
            dlist.append(
                {"stationId": stationId, "stationName": stationName, "trainId": trainNumber, "train_name": train_name,"time": srcArrival, "division_code": division_code})
        newPathList.append((distance, duration, dlist))
    resp = jsonify(newPathList)
    return resp


@path_finder_api.route("/stations", methods=["GET"])
def getAllStationList():
    cursor, conn = connection()
    searchText = request.args.get('searchText')
    sql = f"SELECT * FROM station_master where station_name like '{searchText}%' OR id like '{searchText}%'"
    print(sql)
    cursor.execute(
        f"SELECT * FROM station_master where station_name like '{searchText}%' OR id like '{searchText}%'")
    rows = cursor.fetchall()
    row_count = cursor.rowcount
    resp = jsonify(rows)
    stationDetail = []
    for record in rows:
        stationId = record["id"]
        #sql = f"SELECT * FROM train_schedule where st_train_id_master_id  = {stationId}"
        # print(sql)
        # cursor.execute(sql)
        #r = cursor.fetchall()
        #r_count = cursor.rowcount
        # if(r_count > 0):
        stationDetail.append(str(stationId) + "-" + record["station_name"])
    return jsonify(stationDetail)


def getAllStations():
    cursor, conn = connection()
    cursor.execute("SELECT * FROM station_master")
    rows = cursor.fetchall()
    row_count = cursor.rowcount
    resp = jsonify(rows)
    stationDetail = {}
    for record in rows:
        stationDetail[record["id"]] = record
    return (stationDetail, row_count)


def getAllTrains():
    cursor, conn = connection()
    cursor.execute("SELECT * FROM train_master")
    rows = cursor.fetchall()

    resp = jsonify(rows)
    trainDetail = {}
    for record in rows:
        trainDetail[record["st_train_id_master_id"]] = record["train_name"]
    return trainDetail


@path_finder_api.route("/station-name", methods=["GET"])
def getStationNameByCode():
    cursor, conn = connection()
    stationCode = request.args.get('code')
    print(
        f'SELECT station_name FROM station_master where station_code = "{stationCode}"')
    cursor.execute(
        f'SELECT station_name FROM station_master where station_code = "{stationCode}"')
    rows = cursor.fetchone()
    return rows


@path_finder_api.route("/station-code", methods=["GET"])
def getStationCodeByName():
    cursor, conn = connection()
    name = request.args.get('name')
    print(
        f'SELECT station_code FROM station_master where station_name = "{name}"')
    cursor.execute(
        f'SELECT station_code FROM station_master where station_name = "{name}"')
    rows = cursor.fetchone()
    return rows
