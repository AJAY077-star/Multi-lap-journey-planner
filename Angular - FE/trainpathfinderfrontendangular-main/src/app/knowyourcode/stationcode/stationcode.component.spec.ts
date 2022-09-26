import { ComponentFixture, TestBed } from '@angular/core/testing';

import { StationcodeComponent } from './stationcode.component';

describe('StationcodeComponent', () => {
  let component: StationcodeComponent;
  let fixture: ComponentFixture<StationcodeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ StationcodeComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(StationcodeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
