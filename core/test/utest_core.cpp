#include "core.h"

#include <catch2/catch_test_macros.hpp>

TEST_CASE("example")
{
    CHECK(getRandomNumber() == 4);
}
