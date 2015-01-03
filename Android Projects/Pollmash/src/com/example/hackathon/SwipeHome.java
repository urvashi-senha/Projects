package com.example.hackathon;

import android.os.Bundle;

import java.io.File;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.List;

import com.parse.Parse;
import com.parse.ParseAnalytics;
import com.parse.ParseFile;
import com.parse.ParseObject;
import com.parse.ParseUser;

import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentActivity;
import android.support.v4.view.ViewPager;
import android.support.v4.view.ViewPager.OnPageChangeListener;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TabHost;
import android.widget.TextView;
import android.widget.Toast;
import android.widget.TabHost.OnTabChangeListener;

import android.app.Activity;
import android.content.Intent;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.View.OnClickListener;

public class SwipeHome extends FragmentActivity implements OnTabChangeListener, OnPageChangeListener {

	private static final int REQUEST_PICK_FILE = 1;

    
    
	ParseUser currentUser;
    
    
    public void MessageBox(String message)
    {
       Toast.makeText(this, message, Toast.LENGTH_SHORT).show();
    } 
	
	 MyPageAdapter pageAdapter;
	    private ViewPager mViewPager;
	    private TabHost mTabHost;
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.s_home);
		mViewPager = (ViewPager) findViewById(R.id.viewpager);
		
		Parse.initialize(this, "Q41kE80rWOGz6khmLdhvMPSZd5CJL1YUw35ro9ht", "FaZ2FwBQj8fGCaPblg7T7o6qRX0HwHZNtqIydC68");
			ParseAnalytics.trackAppOpened(getIntent());
		currentUser = ParseUser.getCurrentUser();
       // Tab Initialization
       initialiseTabHost();

       // Fragments and ViewPager Initialization
       List<Fragment> fragments = getFragments();
       pageAdapter = new MyPageAdapter(getSupportFragmentManager(), fragments);
       mViewPager.setAdapter(pageAdapter);
       mViewPager.setOnPageChangeListener(SwipeHome.this);

		
	}
	
	private static void AddTab(SwipeHome activity, TabHost tabHost, TabHost.TabSpec tabSpec) {
       tabSpec.setContent(new MyTabFactory(activity));
       tabHost.addTab(tabSpec);
   }

   // Manages the Tab changes, synchronizing it with Pages
   public void onTabChanged(String tag) {
       int pos = this.mTabHost.getCurrentTab();
       this.mViewPager.setCurrentItem(pos);
   }

   @Override
   public void onPageScrollStateChanged(int arg0) {
   }

   // Manages the Page changes, synchronizing it with Tabs
   @Override
   public void onPageScrolled(int arg0, float arg1, int arg2) {
       int pos = this.mViewPager.getCurrentItem();
       this.mTabHost.setCurrentTab(pos);
   }

   @Override
       public void onPageSelected(int arg0) {
   }
   
   private List<Fragment> getFragments(){
       List<Fragment> fList = new ArrayList<Fragment>();

       // TODO Put here your Fragments
    
       MySampleFragment f1 = MySampleFragment.newInstance("Sample Fragment 1");
       MySampleFragment f2 = MySampleFragment.newInstance("Sample Fragment 2");
      
       fList.add(f1);
       fList.add(f2);
       return fList;
   }


   // Tabs Creation
   private void initialiseTabHost() {
       mTabHost = (TabHost) findViewById(android.R.id.tabhost);
       mTabHost.setup();

       // TODO Put here your Tabs
       final ParseUser currentUser = ParseUser.getCurrentUser();
      
       SwipeHome.AddTab(this, this.mTabHost, this.mTabHost.newTabSpec("Local").setIndicator("Local"));
       SwipeHome.AddTab(this, this.mTabHost, this.mTabHost.newTabSpec("National").setIndicator("National"));
      
       mTabHost.setOnTabChangedListener(this);
      
   }

 
	@Override
	public void onBackPressed() {
		// TODO Auto-generated method stub
		super.onBackPressed();
		Intent intent = new Intent(SwipeHome.this, Welcome.class);
		intent.setFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP);
		intent.putExtra("Exit me", true);
		startActivity(intent);
		finish();
		
	}
	
	
	 @Override
	    public boolean onOptionsItemSelected(MenuItem item) {
	    	
		 if(currentUser.getString("Type").equalsIgnoreCase("Patient"))
		 {
	    	switch(item.getItemId())
	    	{
	    	case R.id.logout : 
	    		Log.i("Check","LOGOUT");
	    		Parse.initialize(this, "e0FVFRBMAWJi5shg4XF8zL3SIuRwDIufww3338so", "toTJmlHTEF43u7PoAFT4fedwqfhoWiSajj1Se7FT");
	    		ParseAnalytics.trackAppOpened(getIntent());
	    		ParseUser.logOut();
	  		Intent intent = new Intent(SwipeHome.this,Welcome.class);
	    		intent.setFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP);
	    	    intent.putExtra("Exit me", true);
				startActivity(intent);
				finish();
	    		return true;
	    	
	    		
	    	default: 
	    		return super.onOptionsItemSelected(item);
	    	
	    	}
		 }
		 else
		 {
			 switch(item.getItemId())
		    	{
		    	case R.id.logout : 
		    		Log.i("Check","LOGOUT");
		    		Parse.initialize(this, "e0FVFRBMAWJi5shg4XF8zL3SIuRwDIufww3338so", "toTJmlHTEF43u7PoAFT4fedwqfhoWiSajj1Se7FT");
		    		ParseAnalytics.trackAppOpened(getIntent());
		    		ParseUser.logOut();
		    		Intent intent = new Intent(SwipeHome.this,Welcome.class);
		    	intent.setFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP);
		    	    intent.putExtra("Exit me", true);
					startActivity(intent);
					finish();
		    		return true;
		    	
		    		
		    	default: 
		    		return super.onOptionsItemSelected(item);
		    	
		    	}
		 }
	    }
	    
		

}