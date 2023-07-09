import {bootstrapApplication} from "@angular/platform-browser";
import {AppComponent} from "./app/app.component";
import {provideAnimations} from '@angular/platform-browser/animations';
import {provideHttpClient} from "@angular/common/http";
import {provideEffects} from "@ngrx/effects";
import {ProjectEffect} from "./app/shared/state/project.effect";
import {importProvidersFrom} from "@angular/core";
import {CommonModule} from "@angular/common";
import {provideStore} from "@ngrx/store";
import {reducer} from "./app/shared/state/project.reducer";
import {provideStoreDevtools} from "@ngrx/store-devtools";


bootstrapApplication(AppComponent, {
  providers: [provideAnimations(),
    provideHttpClient(),
    provideAnimations(),
    importProvidersFrom(CommonModule),
    provideStore({appState: reducer}),
    provideEffects(ProjectEffect),
    provideStoreDevtools(),
  ]
})

