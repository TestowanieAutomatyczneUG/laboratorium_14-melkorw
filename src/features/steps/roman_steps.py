from behave import *
from roman.Roman import arabic_to_roman, roman_to_arabic

use_step_matcher("re")


@given("number equal to (?P<arabic>.+)")
def step_impl(context, arabic):
    context.arabic = int(arabic)


@when("roman number equal to (?P<roman>.+) is taken")
def step_impl(context, roman):
    context.roman = roman


@then("the converted arabic number should be equal to taken roman")
def step_impl(context):
    assert context.roman == arabic_to_roman(context.arabic)

@given("roman number equal to (?P<roman>.+)")
def step_impl(context, roman):
    context.roman = roman


@when("arabic number equal to (?P<arabic>.+) is taken")
def step_impl(context, arabic):
    context.arabic = int(arabic)


@then("the converted roman number should be equal to taken arabic")
def step_impl(context):
    assert context.arabic == roman_to_arabic(context.roman)
