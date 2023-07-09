import {Component} from '@angular/core';
import {ProjectPanelComponent} from "./home/project-panel/project-panel.component";
import {CommonModule} from "@angular/common";

@Component({
  standalone: true,
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  imports: [
    ProjectPanelComponent,
    CommonModule,
  ],
  providers: []
})
export class AppComponent {
}
