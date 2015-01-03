package com.example.hackathon;

public class Patient {
	private String picName;
	private String picParty;
	private String picState;
	private String picConstituency;
	private String picPosition;
	private int picStockRate;
	private String picId;
	
	public Patient(String picName,String picParty, String picState,String picConstituency,
			String picPosition,int picStockRate, String picId)
	{ 
		 this.picName=picName;
	     this.picParty=picParty;
	     this.picState=picState;
	     this.picConstituency=picConstituency;
	     this.picPosition=picPosition;
	     this.picStockRate=picStockRate;
	     this.picId = picId;
	}
	
	public String getPicId()
	{
		return this.picId;
	}
	public String getPicName()
	{
		return this.picName;
	}
	public String getPicParty()
	{
		return this.picParty;
	}
    public String getPicState()
    {
    	return this.picState;
    }
    public String getPicConstituency()
    {
    	return this.picConstituency;
    }
    public String getPicPosition()
    {
    	return this.picPosition;
    }
    public int getpicStockRate()
    {
    	return this.picStockRate;
    }
    }
