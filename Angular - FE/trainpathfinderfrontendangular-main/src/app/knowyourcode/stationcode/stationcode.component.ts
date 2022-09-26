import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { HttpService } from 'src/app/HttpService';

@Component({
  selector: 'app-stationcode',
  templateUrl: './stationcode.component.html',
  styleUrls: ['./stationcode.component.css']
})
export class StationcodeComponent implements OnInit {

  stationCode: string;
  stationName: string;

  stationCodeFormGroup = new FormGroup({
    name: new FormControl("")
  });

  stationNameFormGroup = new FormGroup({
    code: new FormControl("")
  });

  constructor(private _httpService: HttpService) { }

  ngOnInit(): void {
  }

  onStationNameCheckClick() {
    let name = this.stationCodeFormGroup.get("name").value
    this._httpService.getStationCodeByName(name).subscribe((response) => {
      console.log(response)
      this.stationCode = response["station_code"]
    })
  }

  onStationCodeCheckClick() {
    let code = this.stationNameFormGroup.get("code").value
    this._httpService.getStationNameByCode(code).subscribe((response) => {
      this.stationName = response["station_name"]
    })
  }
}
