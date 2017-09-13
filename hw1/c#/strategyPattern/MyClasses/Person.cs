using System.Collections.Generic;
using System.IO;
using System.Runtime.Serialization.Json;

namespace MyClasses
{
    public class Person
    {
        public string BirthCounty{get; set;}
        public string BirthDay {get; set;}
        public string BirthMonth {get; set;}
        public string BirthOrder {get; set;}
        public string BirthYear {get; set;}
        public string FirstName {get; set;}
        public string Gender {get; set;}
        public string IsPartOfMultipleBirth {get; set;}
        public string LastName {get; set;}
        public string MiddleName {get; set;}
        public string MotherFirstName {get; set;}
        public string MotherLastName {get; set;}
        public string MotherMiddleName {get; set;}
        public string NewbornScreeningNumber {get; set;}
        public string ObjectId {get; set;}
        public string Phone1 {get; set;}
        public string Phone2 {get; set;}
        public string SocialSecurityNumber {get; set;}
        public string StateFileNumber {get; set;}        
    
    public override string ToString(){
        return "Id=" + ObjectId + ", Name="+FirstName+ MiddleName+ LastName + ", Birthday="+BirthDay+"/"+BirthMonth+"/"+BirthYear;
    }

    }
}
