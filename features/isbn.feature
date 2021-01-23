Feature: Control Number
  Check if given number is correct

  Scenario Outline: Wrong length of value
    Given isbn number equal to <isbn>
    When length of isbn number is different than 13
    Then result should be equal to given string <result>

    Examples:
      | isbn                    | result                 |
      | 3-123-22                | Wrong length of values |
      | 331112222223212333-2323 | Wrong length of values |
      | 2                       | Wrong length of values |

  Scenario Outline: Wrong type of characters
    Given isbn number with characters equal to <isbn>
    When type of characters is different than integers or -
    Then bad type result should be equal to given string <bad_type_result>

    Examples:
      | isbn                | bad_type_result             |
      | 3-12-3-567-8-12-abc | Provide only numbers please |
      | abcdefqwert-yu      | Provide only numbers please |
      | a-12345678901-b     | Provide only numbers please |

  Scenario Outline: Checking if control number is correct
    Given correct isbn number equal to <isbn>
    When using check_isbn function
    Then result should be equal to <result>
    Examples:
      | isbn              | result |
      | 978-3-16-148410-0 | True   |
      | 978-3-16-148423-0 | True   |
      | 978-3-16-148423-1 | False  |