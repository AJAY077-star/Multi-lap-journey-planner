import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class HttpService {
  private url = 'http://localhost:5000/api/v1/path';

  constructor(private http: HttpClient) { }

  findRoute(source: number, destination: number) {
    return this.http.get(
      `${this.url}/finder?source=${source}&destination=${destination}`
    );
  }

  searchStation(searchText: string) {
    return this.http.get(`${this.url}/stations?searchText=${searchText}`);
  }

  getStationCodeByName(name: string): Observable<string> {
    return this.http.get<string>(`${this.url}/station-code?name=${name}`);
  }

  getStationNameByCode(code: string): Observable<string> {
    return this.http.get<string>(`${this.url}/station-name?code=${code}`);
  }
}
