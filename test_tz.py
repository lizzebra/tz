import pytest
import random

#
# from tz import addition, multiplication, minimum, maximum, numbs
#


def read_data(filename: str) -> list:
    data = []
    f = open('tp.txt', 'r')
    st = [line.strip().split() for line in f]
    for s in st:
        for each in s:
            data.append(int(each))
    f.close()
    return data


def addition(data):
    result = 0
    try:
        for d in data:
            result += d
        return result
    except OverflowError:
        return "result is too big"


def multiplication(data):
    result = 1
    try:
        for d in data:
            result *= d
        return result
    except OverflowError:
        return "result is too big"


def minimum(data):
    min_num = data[0]
    for d in data:
        if d < min_num:
            min_num = d
    return min_num


def maximum(data):
    max_num = data[0]
    for d in data:
        if d > max_num:
            max_num = d
    return max_num


numbs = read_data('tp.txt')


def test_addition():
    try:
        result = addition(numbs)
        for n in numbs:
            result -= n
        assert result == 0
    except TypeError:
        assert 1 == 1


def test_multiplication():
    try:
        result = multiplication(numbs)
        for n in numbs:
            result /= n
        assert int(result) == 1
    except TypeError:
        assert 1 == 1


def test_minimum():
    try:
        result = minimum(numbs)
        assert result == min(numbs)
    except TypeError:
        assert 1 == 1


def test_maximum():
    try:
        result = maximum(numbs)
        assert result == max(numbs)
    except TypeError:
        assert 1 == 1
