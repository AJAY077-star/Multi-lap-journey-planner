import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FindrouteComponent } from './findroute.component';

describe('FindrouteComponent', () => {
  let component: FindrouteComponent;
  let fixture: ComponentFixture<FindrouteComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ FindrouteComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(FindrouteComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
