package com.example.hackathon;

public class Comments {
	private String picName;
	private String picBy;
	
	public Comments(String picName,String picBy)
	{ 
		 this.picName=picName;
	     this.picBy=picBy;
	     
	}
	
	public String getPicBy()
	{
		return this.picBy;
	}
	public String getPicName()
	{
		return this.picName;
	}
	
	
}
