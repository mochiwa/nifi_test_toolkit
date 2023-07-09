/// <reference types="cypress" />

describe('list project', () => {
  const projectPanel = '[data-tst="project_panel"]';

  beforeEach(() => {
    cy.visit('localhost:4200');
  });

  it('should display an empty project panel when backend return empty panel', () => {
    cy.intercept('GET', '**/projects', {
      statusCode: 200,
      body: [],
    }).as("GET");

    cy.wait('@GET').then(({request}) => {
      cy.get(projectPanel).within(() => {
        cy.get("mat-accordion").should("not.be.visible")
      });
    })
  });

  it('should display project panel with one expansion-panel when backend return one project', () => {
    cy.intercept('GET', '**/projects', {
      statusCode: 200,
      body: [
        {
          'project_id': "123",
          'project_name': "my project",
          'project_uri': "http://localhost",
          'authentication': true,
          'username': "username",
          'password': "password",
        }
      ],
    }).as("GET");

    cy.wait('@GET').then(({request}) => {
      cy.get(projectPanel).within(() => {
        cy.get("[id=project-panel-123]").should("be.visible")
        cy.get("mat-panel-title").contains("my project")
      }).should('be.visible');
    })
  });
})
