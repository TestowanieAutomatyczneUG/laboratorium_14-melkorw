Feature: Convert Numbers
  Converting Arabic to Roman Numbers and opposite

  Scenario Outline: Convert arabic number to roman
    Given number equal to <arabic>
    When roman number equal to <roman> is taken
    Then the converted arabic number should be equal to taken roman

    Examples:
      | arabic | roman     |
      |  1     | I         |
      |  4     | IV        |
      |  28    | XXVIII    |
      |  333   | CCCXXXIII |
      |  922   | CMXXII    |
      |  1300  | MCCC      |
      |  1579  | MDLXXIX   |
      |  2100  | MMC       |


  Scenario Outline: Convert roman number to arabic
    Given roman number equal to <roman>
    When arabic number equal to <arabic> is taken
    Then the converted roman number should be equal to taken arabic

    Examples:
     | roman     | arabic |
     | I         | 1      |
     | IV        | 4      |
     | XXVIII    | 28     |
     | CCCXXXIII | 333    |
     | CMXXII    | 922    |
     | MCCC      | 1300   |
     | MDLXXIX   | 1579   |
     | MMC       | 2100   |