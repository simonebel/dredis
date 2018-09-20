import time

from tests.helpers import fresh_redis


PROFILE_PORT = 6376
LARGE_NUMBER = 1000


def test_zadd():
    r = fresh_redis(port=PROFILE_PORT)
    before_zadd = time.time()
    for score in range(LARGE_NUMBER):
        assert r.zadd('myzset', 0, 'value{}'.format(score)) == 1
    after_zadd = time.time()
    print '\nZADD time = {}s'.format(after_zadd - before_zadd)


def test_zcard():
    r = fresh_redis(port=PROFILE_PORT)
    for score in range(LARGE_NUMBER):
        assert r.zadd('myzset', 0, 'value{}'.format(score)) == 1
    before_zcard = time.time()
    assert r.zcard('myzset') == LARGE_NUMBER
    after_zcard = time.time()
    print '\nZCARD time = {}s'.format(after_zcard - before_zcard)


def test_zrank():
    r = fresh_redis(port=PROFILE_PORT)
    for score in range(LARGE_NUMBER):
        assert r.zadd('myzset', 0, 'value{}'.format(score)) == 1
    before_zrank = time.time()
    assert r.zrank('myzset', 'value{}'.format(LARGE_NUMBER - 1)) == LARGE_NUMBER - 1
    after_zrank = time.time()

    print '\nZRANK time = {}s'.format(after_zrank - before_zrank)


def test_zcount():
    r = fresh_redis(port=PROFILE_PORT)
    for score in range(LARGE_NUMBER):
        assert r.zadd('myzset', 0, 'value{}'.format(score)) == 1
    before_zcount = time.time()
    assert r.zcount('myzset', '-inf', '+inf') == LARGE_NUMBER
    after_zcount = time.time()

    print '\nZCOUNT time = {}s'.format(after_zcount - before_zcount)
