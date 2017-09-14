using System.Collections.Generic;
using System;

namespace MyClasses
{
    public class MatcherTwo : Matcher 
    {

        public override PairList FindMatches(PersonCollection inPersonCol)
    	{	
    		PairList result = new PairList();
    		
    		for (int i = 0 ; i < inPersonCol.Length ; i++){
    			for (int j = 0 ; j < inPersonCol.Length ; j++){
    				if (j <= i) {
    					continue;
    				}
    				else {
    					if (inPersonCol[i].FirstName == inPersonCol[j].FirstName && inPersonCol[i].LastName == inPersonCol[j].LastName
                                && inPersonCol[i].SocialSecurityNumber == inPersonCol[j].SocialSecurityNumber){
    						// this is where we are going to want to put our matcher and personmatch class
    						// still trying to decide if a pair class is a good  call or not.. i mean why not right?
    						Pair tempPair = new Pair(inPersonCol[i], inPersonCol[j]);
    						result.Add(tempPair);

    						break;
    					}
    				}
    			}
    		}
    		return result;
    	}
    	

    }
 }