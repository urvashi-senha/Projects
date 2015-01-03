package com.example.health_connect;

public class Picture {
	private String picName;
	private String picType;
	private int picDrawable;
	
	public Picture(String picName,String picType, int picDrawable)
	{ 
		 this.picName=picName;
	     this.picType=picType;
	     this.picDrawable=picDrawable;
		
	}
	
	public String getPicName()
	{
		return this.picName;
	}
    public String getPicType()
    {
    	return this.picType;
    }
    public int getPicSource()
    {
    	return this.picDrawable;
    }
}
