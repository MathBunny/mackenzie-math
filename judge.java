/* Programming Competition - Template (Horatiu Lazu) */

import java.io.*;
import java.util.*;
import java.lang.*;
import java.awt.*;
import java.awt.geom.*;
import java.math.*;
import java.nio.channels.*;

class Person implements Comparable<Person>{
	private String name;
	private int score;
	
	public Person(String name, int score){
		this.name = name;
		this.score = score;	
	}
	
	public String getName(){
		return this.name;	
	}
	
	public int getScore(){
		return this.score;	
	}
	
	public int compareTo(Person o){
		if (o.getScore() <= score)
			return 0;
		return 1;
	}
		
}


class Main{
	public static void main (String [] args){
		new Main();
	}

	public Main(){
		try{
			BufferedReader in;
			in = new BufferedReader (new InputStreamReader (System.in)); //Used for CCC
			
			ArrayList<Person> people = new ArrayList<Person>();
			while(true){
				String input = in.readLine();
				if (input == null || input.equals(""))
					break;
				StringTokenizer st = new StringTokenizer(in.readLine());
				people.add(new Person(st.nextToken(), Integer.parseInt(st.nextToken())));
			}
			Collections.sort(people);
			for(int i = 0; i < people.size(); i++){
				System.out.println("<tr><td><p><center>" + people.get(i).getName() + "</center></p></td><td><center>" + people.get(i).getScore() + "</center></td></tr>");	
			}
			
		}
		catch(IOException e){
			System.out.println("IO: General");
		}
	}
}