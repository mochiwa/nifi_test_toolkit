/// <reference types="cypress" />

describe('list project', () => {
  const projectPanel = '[data-tst="project_panel"]';

  beforeEach(() => {
    cy.visit('localhost:4200');
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
    cy.wait("@GET")
  });

  it('should remove the [id=project-panel-123] when click on delete button', () => {
    cy.intercept('DELETE', '**/projects/123', {
      statusCode: 201,
      body: null
    }).as("DELETE");
    cy.intercept('GET', '**/projects', {
      statusCode: 200,
      body: [],
    }).as("GET");

    cy.get(projectPanel).within(() => {
      cy.get("[id=project-panel-123] button").click()
      cy.wait('@DELETE').then(()=>{
        cy.wait("@GET").then(()=>{
          cy.get("[id=project-panel-123]").should("not.exist")
        })
      })
    });
  });
})
