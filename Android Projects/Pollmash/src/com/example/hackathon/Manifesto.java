package com.example.hackathon;

public class Manifesto {
	private String picPolitician;
	private String picContent;
	private String picHas_done;
	
	public Manifesto(String picPolitician, String picContent,String picHas_done)
	{ 
		 this.picPolitician=picPolitician;
		 this.picContent=picContent;
		 this.picHas_done=picHas_done;
		 
	     
	}
	
	public String getpicPolitician()
	{
		return this.picPolitician;
	}
	public String getpicContent()
	{
		return this.picContent;
	}
	public String getpicHas_done()
	{
		return this.picHas_done;
	}
	
	
}
