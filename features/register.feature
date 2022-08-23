Feature: Register Page

    Scenario: User can register
        Given open browser
        When open danabijak site
        Then user can access register page
        And user input ktp
        And user input phone number
        And user input email register
        And user input password register
        And user input password confirmation
        And user click checkbox syarat dan ketentuan
        And user click create account