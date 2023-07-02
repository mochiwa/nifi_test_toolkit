import { Component } from '@angular/core';
import {ProjectPanelComponent} from "./home/project-panel/project-panel.component";

@Component({
  standalone:true,
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  imports:[
    ProjectPanelComponent
  ]
})
export class AppComponent {
}
