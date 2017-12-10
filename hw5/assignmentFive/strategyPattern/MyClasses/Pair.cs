using System.Collections.Generic;

namespace MyClasses
{
    public class Pair 
    {
       public Person First {get; set;}
       public Person Second {get; set;}

       public Pair(Person infirst, Person insecond){
       		First = infirst;
       		Second = insecond;
       }

       public override string ToString(){
       	return First.ToString() + "\n" + Second.ToString() + "\n"; 
       }
       
    }
}