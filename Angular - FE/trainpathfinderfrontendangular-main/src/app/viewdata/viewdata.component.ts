import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-viewdata',
  templateUrl: './viewdata.component.html',
  styleUrls: ['./viewdata.component.css']
})
export class ViewdataComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

  zones=[
    {
      id: 1,
      zonecode: "ECOR",
      zonename: "EAST COAST RAILWAY"
    },
    {
      id: 2,
      zonecode: "ER",
      zonename: "EASTERN RAILWAY"
    },
    {
      id: 3,
      zonecode: "KRCL",
      zonename: "KONKAN RAILWAY"
    },
    {
      id: 4,
      zonecode: "NCR",
      zonename: "NORTH CENTRAL RAILWAY"
    },
    {
      id: 5,
      zonecode: "NER",
      zonename: "NORTH EASTERN RAILWAY"
    },
    {
      id: 6,
      zonecode: "NFR",
      zonename: "NORTH FRONTIER RAILWAY"
    },
    {
      id: 7,
      zonecode: "NR",
      zonename: "NORTHERN RAILWAY"
    },
    {
      id: 8,
      zonecode: "NWR",
      zonename: "NORTH WESTERN RAILWAY"
    },
    {
      id: 9,
      zonecode: "PR",
      zonename: "PAKISTAN RAILWAY"
    },
    {
      id: 10,
      zonecode: "SECR",
      zonename: "SOUTHEAST CENTRAL RAILWAY"
    },
    {
      id: 11,
      zonecode: "SCR",
      zonename: "SOUTH CENTRAL RAILWAY"
    },
    {
      id: 12,
      zonecode: "SER",
      zonename: "SOUTH EASTERN RAILWAY"
    },
    {
      id: 13,
      zonecode: "SR",
      zonename: "SOUTHERN RAILWAY"
    },
    {
      id: 14,
      zonecode: "SWR",
      zonename: "SOUTH WESTERN RAILWAY"
    },
    {
      id: 15,
      zonecode: "WCR",
      zonename: "WEST CENTRAL RAILWAY"
    },
    {
      id: 16,
      zonecode: "WR",
      zonename: "WESTERN RAILWAY"
    },
    {
      id: 17,
      zonecode: "BR",
      zonename: "BANGLADESH RAILWAY"
    },
    {
      id: 18,
      zonecode: "CPT",
      zonename: "KOLKATA PORT TRUSTRAILWAY"
    },
    {
      id: 19,
      zonecode: "DFCR",
      zonename: "DEDICATED FREIGHT CORRIDO"
    },
    {
      id: 20,
      zonecode: "CP",
      zonename: "CHENNAI PORT TRUSTRAILWAY"
    },
    {
      id: 21,
      zonecode: "CR",
      zonename: "CENTRAL RAILWAY"
    },
    {
      id: 22,
      zonecode: "ECR",
      zonename: "EAST CENTRAL RAILWAY"
    }
  ]
}
