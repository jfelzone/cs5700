using System.Collections.Generic;

namespace MyClasses
{
    public class Pair 
    {
       public Person First {get; set;}
       public Person Second {get; set;}

       public Pair(first, second){
       	this.First = first;
       	this.Second = second;
       }

       
    }
}