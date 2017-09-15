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
            Assert.NotEqual(testInput.Name, "tester");
        }

        [Fact]
        public void Test2(){
            MatcherOne resultingMatcher = new MatcherOne();
            JsonInput temp = new JsonInput();
            PersonCollection personList = new PersonCollection(temp, "filename");
            Person bob = new Person();
            Person joe = new Person();
            bob.FirstName = "bob"; bob.LastName = "Texas";
            joe.FirstName = "joe"; joe.LastName = "Texas";
            personList.Add(bob);
            personList.Add(joe);
            PairList resultingPairList = resultingMatcher.FindMatches(personList);

            Assert.Equal(resultingPairList.Count, 0);
        }

        [Fact]
        public void Test3(){
            MatcherOne resultingMatcher = new MatcherOne();
            JsonInput temp = new JsonInput();
            PersonCollection personList = new PersonCollection(temp, "filename");
            Person bob = new Person();
            Person joe = new Person();
            bob.FirstName = "bob"; bob.LastName = "Texas";
            joe.FirstName = "bob"; joe.LastName = "Texas";
            personList.Add(bob);
            personList.Add(joe);
            PairList resultingPairList = resultingMatcher.FindMatches(personList);

            Assert.Equal(resultingPairList.Count, 1);
        }


        [Fact]
        public void Test4(){
            MatcherThree resultingMatcher = new MatcherThree();
            JsonInput temp = new JsonInput();
            PersonCollection personList = new PersonCollection(temp, "filename");
            Person bob = new Person();
            Person joe = new Person();
            bob.FirstName = "bob"; bob.LastName = "Texas";
            joe.FirstName = "bob"; joe.LastName = "Texas";
            bob.BirthDay = "1"; bob.BirthMonth = "12"; bob.BirthYear = "1978";
            joe.BirthDay = "1"; joe.BirthMonth = "12"; joe.BirthYear = "1978";
            personList.Add(bob);
            personList.Add(joe);
            PairList resultingPairList = resultingMatcher.FindMatches(personList);

            Assert.Equal(resultingPairList.Count, 1);
        }

        [Fact]
        public void Test5(){
            MatcherThree resultingMatcher = new MatcherThree();
            JsonInput temp = new JsonInput();
            PersonCollection personList = new PersonCollection(temp, "filename");
            Person bob = new Person();
            Person joe = new Person();
            bob.FirstName = "bob"; bob.LastName = "Texas";
            joe.FirstName = "bob"; joe.LastName = "Texas";
            bob.BirthDay = "1"; bob.BirthMonth = "12"; bob.BirthYear = "1978";
            joe.BirthDay = "1"; joe.BirthMonth = "10"; joe.BirthYear = "1978";
            personList.Add(bob);
            personList.Add(joe);
            PairList resultingPairList = resultingMatcher.FindMatches(personList);

            Assert.Equal(resultingPairList.Count, 0);
        }

    }
}