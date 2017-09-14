using System.Collections.Generic;
using System;

namespace MyClasses
{
    public class MatcherThree : Matcher 
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
                        string person1Birth = null;
                        string person2Birth = null;
                        person1Birth = inPersonCol[i].BirthDay+'/'+inPersonCol[i].BirthMonth+'/'+inPersonCol[i].BirthYear;
                        person2Birth = inPersonCol[j].BirthDay+'/'+inPersonCol[j].BirthMonth+'/'+inPersonCol[j].BirthYear;
                            // testing the output of this and making sure it was comparing the correct thing
                        // Console.WriteLine("dates for comparison:");
                        // Console.WriteLine('\t'+person1Birth);
                        // Console.WriteLine('\t'+person2Birth);
    					if (
                                inPersonCol[i].FirstName == inPersonCol[j].FirstName 
                                && inPersonCol[i].LastName == inPersonCol[j].LastName
                                //&& inPersonCol[i].SocialSecurityNumber == inPersonCol[j].SocialSecurityNumber
                                &&
                                 person1Birth == person2Birth){
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