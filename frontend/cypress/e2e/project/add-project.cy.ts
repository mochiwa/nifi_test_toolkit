describe('add a project', () => {
  const addProjectButton = '[data-tst="add_project-btn"]'
  const addProjectForm = '[data-tst="add_project-form"]'

  beforeEach(() => {
    cy.visit('localhost:4200');
  })

  it('should display a button to add project', () => {
    cy.get(addProjectButton).should('be.visible');
  });
  it('should display a form to add project when click add project btn', () => {
    cy.get(addProjectButton).click();
    cy.get(addProjectForm).should('be.visible');
  })
  it('should hide add project form when click cancel btn', () => {
    cy.get(addProjectButton).click();
    cy.get(addProjectForm).contains("Cancel").click();

    cy.get(addProjectForm).should('not.exist');
  });
  describe("form validation", () => {
    beforeEach(() => {
      //cy.visit('localhost:4200');
      cy.get(addProjectButton).click()
      cy.get(addProjectForm).within(() => {
        cy.get('input[name="project_name"]').type("the project name")
        cy.get('input[name="project_uri"]').type("http://localhost")
        cy.get('input[name="authentication"]').check()
        cy.get('input[name="username"]').type("username")
        cy.get('input[name="password"]').type("password")
      })
    })
    it('should close form when submit it', () => {
      cy.get(addProjectForm).contains('Submit').should('be.enabled').click()
      //add rest interceptor
      cy.get(addProjectForm).should('not.exist')
    });
    it('should display "project name is required" when project name is empty', () => {
      cy.get(addProjectForm).contains('input[name="project_name"]').clear()
      cy.get("div").contains('project name is required.')
      cy.get(addProjectForm).contains('Submit').should('be.disabled')
      cy.get(addProjectForm).should('exist')
    });
    it('should disabled field username and password when authentication is unchecked', () => {
      cy.get(addProjectForm).contains('input[name="authentication"]').uncheck()
      cy.get(addProjectForm).contains('input[name="username"]').should('be.disabled')
      cy.get(addProjectForm).contains('input[name="password"]').should('be.disabled')
      //add rest interceptor
      cy.get(addProjectForm).contains('Submit').should('be.enabled').click()
    });
    it('should display authentication error when authentication is checked but empty input', () => {
      cy.get(addProjectForm).contains('input[name="username"]').clear()
      cy.get(addProjectForm).contains('input[name="password"]').clear()

      cy.get("div").contains('username is required.')
      cy.get("div").contains('password is required.')
      cy.get(addProjectForm).contains('Submit').should('be.disabled')
    });
  })


});


