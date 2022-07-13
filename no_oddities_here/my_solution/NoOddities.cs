using System;
using System.Collections;
using System.Linq;

public class NoOddities
{
  public static int[] NoOdds(int[] values) 
  {
    int[] evens = new int[] {};
    foreach(int i in values){
      if (i % 2 == 0) {
        evens = evens.Concat(new int[] { i }).ToArray();
      }
    }
    return evens;
  }
}