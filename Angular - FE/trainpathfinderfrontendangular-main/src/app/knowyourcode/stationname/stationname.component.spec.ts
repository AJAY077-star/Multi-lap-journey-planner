import { ComponentFixture, TestBed } from '@angular/core/testing';

import { StationnameComponent } from './stationname.component';

describe('StationnameComponent', () => {
  let component: StationnameComponent;
  let fixture: ComponentFixture<StationnameComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ StationnameComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(StationnameComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
