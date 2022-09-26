import { Component, Input, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';
import { debounceTime, finalize, Observable, switchMap, tap } from 'rxjs';
import { HttpService } from '../HttpService';

@Component({
  selector: 'app-findroute',
  templateUrl: './findroute.component.html',
  styleUrls: ['./findroute.component.css'],
})
export class FindrouteComponent implements OnInit {
  sourceControl = new FormControl('');
  destinationControl = new FormControl('');

  sourceFilteredStations: string[];
  destinationFilteredStations: string[];
  routeInfo: any;

  constructor(private httpService: HttpService) {}

  ngOnInit() {
    //this._findRoute();
    this._sourceStationAutoComplete();
    this._destinationStationAutoComplete();
  }

  private _sourceStationAutoComplete() {
    this.sourceControl.valueChanges
      .pipe(
        debounceTime(500),
        tap(() => {
          this.sourceFilteredStations = [];
        }),
        switchMap((value) =>
          this.httpService.searchStation(value).pipe(finalize(() => {}))
        )
      )
      .subscribe((data: string[]) => {
        console.log(data);
        if (data == undefined) {
          this.sourceFilteredStations = [];
        } else {
          this.sourceFilteredStations = data;
        }
        console.log(this.sourceFilteredStations);
      });
  }

  private _destinationStationAutoComplete() {
    this.destinationControl.valueChanges
      .pipe(
        debounceTime(500),
        tap(() => {
          this.sourceFilteredStations = [];
        }),
        switchMap((value) =>
          this.httpService.searchStation(value).pipe(finalize(() => {}))
        )
      )
      .subscribe((data: string[]) => {
        console.log(data);
        if (data == undefined) {
          this.sourceFilteredStations = [];
        } else {
          this.sourceFilteredStations = data;
        }
        console.log(this.sourceFilteredStations);
      });
  }

  private _findRoute(sourceId: number, destinationId: number) {
    this.httpService.findRoute(sourceId, destinationId).subscribe(
      (response) => {
        console.log(response);
        this.routeInfo = response;
      },
      (error) => {
        console.log(error);
      }
    );
  }

  onCheckTrainClick() {
    let sourceValue = this.sourceControl.value;
    let destinatonValue = this.destinationControl.value;
    let sourceStationId = sourceValue.split('-')[0];
    let destinationStationId = destinatonValue.split('-')[0];

    if (sourceStationId == destinationStationId) {
      alert('Source and destination should be different');
    }
    this._findRoute(sourceStationId, destinationStationId);
    console.log(
      'source value = ' + sourceValue + ' - destination = ' + destinatonValue
    );
  }

  onDestinationChange($event) {
    console.log(this.destinationControl);
  }

  onSourceChange($event) {
    console.log(this.sourceControl);
  }

  refresh(): void {
    //window.location.reload();
    this.sourceControl.reset();
    this.destinationControl.reset();
    this.routeInfo = null;
  }
}

export interface Brand {
  value: string;
  viewValue: string;
}
