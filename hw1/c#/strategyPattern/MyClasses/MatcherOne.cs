using System.Collections.Generic;

namespace MyClasses
{
    public class MatcherOne : Matcher 
    {

        public override void FindMatches(PersonCollection inPersonCol)
    	{
    		for (int i = 0 ; i < inPersonCol.Length ; i++){
    			for (int j = 0 ; j < inPersonCol.Length ; j++){
    				if (j <= i) {
    					continue;
    				}
    				else {
    					if (inPersonCol[i].FirstName == inPersonCol[j].FirstName){
    						// this is where we are going to want to put our matcher and personmatch class
    						// still trying to decide if a pair class is a good  call or not.. i mean why not right?
    						

    						// ok, just cuz im not sure where else to put my thoughts right now
    						// so i think i want a pair class (which will contain two people)
    						// and then i think i want a par list class (which will have a list of pairs)
    						// and then i want an output class (abstract class of outputs)
    						// and then i want out output strategy classes (console and file as of right now (so just two))
    						// the goal is that to a pair list collection dealio, i should be able to call the output strategy and get a result

    						continue;
    					}
    				}
    			}
    		}
    	}
    	

    }
 }