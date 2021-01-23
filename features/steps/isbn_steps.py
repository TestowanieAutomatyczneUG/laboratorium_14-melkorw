from behave import *
from isbn.isbn import check_isbn

use_step_matcher("re")


@given("isbn number equal to (?P<isbn>.+)")
def step_impl(context, isbn):
    context.isbn = isbn


@when("length of isbn number is different than 13")
def step_impl(context):
    context.isbn_result = check_isbn(context.isbn)


@then("result should be equal to given string (?P<result>.+)")
def step_impl(context, result):
    assert context.isbn_result == result

@given("isbn number with characters equal to (?P<isbn>.+)")
def step_impl(context, isbn):
    context.isbn = isbn


@when("type of characters is different than integers or -")
def step_impl(context):
    context.isbn_result = check_isbn(context.isbn)


@then("bad type result should be equal to given string (?P<bad_type_result>.+)")
def step_impl(context, bad_type_result):
    assert context.isbn_result == bad_type_result


@given("correct isbn number equal to (?P<isbn>.+)")
def step_impl(context, isbn):
    context.isbn = isbn


@when("using check_isbn function")
def step_impl(context):
    context.isbn_result = check_isbn(context.isbn)


@then("result should be equal to (?P<result>.+)")
def step_impl(context, result):
    print(bool(result))
    if result == 'True':
        res = True
    else:
        res = False
    assert context.isbn_result == res
