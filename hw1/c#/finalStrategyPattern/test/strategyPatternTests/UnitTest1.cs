using System;
using Xunit;
using MyClasses;

namespace unit_testing_using_dotnet_unit_tests
{
    public class UnitTest1
    {
        [Fact]
        public void Test1()
        {
            JsonInput testInput = new JsonInput();
            testInput.Name = "test";
            Assert.Equal(testInput.Name, "tester");
        }
    }
}