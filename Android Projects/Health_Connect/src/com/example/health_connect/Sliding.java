package com.example.health_connect;

import android.view.animation.AccelerateInterpolator;
import android.view.animation.Animation;
import android.view.animation.TranslateAnimation;
import android.widget.ViewFlipper;

public class Sliding {
	
	public static void slideFromRightToLeft(int newSlide,ViewFlipper viewFliper) {
		viewFliper.setInAnimation(inFromRightAnimation());
		viewFliper.setOutAnimation(outToLeftAnimation());
		viewFliper.setDisplayedChild(newSlide);
		
	}

	

	public static void slideFromLeftToRight(int newSlide, ViewFlipper viewFliper) {
	
		viewFliper.setInAnimation(inFromLeftAnimation());
		viewFliper.setOutAnimation(outToRightAnimation());
		viewFliper.setDisplayedChild(newSlide);
		
	}

	
	public static void slideTimer(int newSlide, ViewFlipper viewFliper) {
		viewFliper.setInAnimation(inFromRightAnimation());
		viewFliper.setOutAnimation(outToLeftAnimation());
		viewFliper.setDisplayedChild(newSlide);
	}
	
	public static void slideFromDownToUpEdit(int newSlide,ViewFlipper viewFliper) {
		viewFliper.setInAnimation(inFromDownAnimation());
		viewFliper.setOutAnimation(outToUpAnimation());
		viewFliper.setDisplayedChild(newSlide);
		
	}
	
	public static void slideFromUpToDownEdit(int newSlide,ViewFlipper viewFliper) {
		viewFliper.setInAnimation(inFromUpAnimation());
		viewFliper.setOutAnimation(outToDownAnimation());
		viewFliper.setDisplayedChild(newSlide);
		
	}
	/**
	 * @param: N/A
	 * @Objective : Slide style of new screen (Appear)
	 * @category:
	 */
	public static Animation inFromRightAnimation() {
		Animation inFromRight = new TranslateAnimation(
				Animation.RELATIVE_TO_PARENT, +1.0f,
				Animation.RELATIVE_TO_PARENT, 0.0f,
				Animation.RELATIVE_TO_PARENT, 0.0f,
				Animation.RELATIVE_TO_PARENT, 0.0f);
		inFromRight.setDuration(500);// 500
		inFromRight.setInterpolator(new AccelerateInterpolator());
		return inFromRight;
	}

	/**
	 * @param: N/A
	 * @Objective : Slide style of old screen (away)
	 * @category:
	 */
	public static Animation outToLeftAnimation() {
		Animation outtoLeft = new TranslateAnimation(
				Animation.RELATIVE_TO_PARENT, 0.0f,
				Animation.RELATIVE_TO_PARENT, -1.0f,
				Animation.RELATIVE_TO_PARENT, 0.0f,
				Animation.RELATIVE_TO_PARENT, 0.0f);
		outtoLeft.setDuration(500);// 500
		outtoLeft.setInterpolator(new AccelerateInterpolator());
		return outtoLeft;
	}

	public static Animation inFromLeftAnimation() {
		Animation inFromRight = new TranslateAnimation(
				Animation.RELATIVE_TO_PARENT, -1.0f,
				Animation.RELATIVE_TO_PARENT, 0.0f,
				Animation.RELATIVE_TO_PARENT, 0.0f,
				Animation.RELATIVE_TO_PARENT, 0.0f);
		inFromRight.setDuration(500);
		inFromRight.setInterpolator(new AccelerateInterpolator());
		return inFromRight;
	}

	public static Animation outToRightAnimation() {
		Animation outtoLeft = new TranslateAnimation(
				Animation.RELATIVE_TO_PARENT, 0.0f,
				Animation.RELATIVE_TO_PARENT, +1.0f,
				Animation.RELATIVE_TO_PARENT, 0.0f,
				Animation.RELATIVE_TO_PARENT, 0.0f);
		outtoLeft.setDuration(500);
		outtoLeft.setInterpolator(new AccelerateInterpolator());
		return outtoLeft;
	}
	
/////////////---In from Up, out from down---//////////
	public static Animation inFromUpAnimation() {
	Animation inFromRight = new TranslateAnimation(
			///X coordinator
			Animation.RELATIVE_TO_PARENT,  0.0f, Animation.RELATIVE_TO_PARENT,  0.0f,
			// Y coodinator
			Animation.RELATIVE_TO_PARENT,  -1.0f, Animation.RELATIVE_TO_PARENT,   0.0f
			);
	inFromRight.setDuration(500);
	inFromRight.setInterpolator(new AccelerateInterpolator());
	return inFromRight;
}
	public static Animation outToDownAnimation() {
	Animation outtoLeft = new TranslateAnimation(
			Animation.RELATIVE_TO_PARENT,  0.0f, Animation.RELATIVE_TO_PARENT,  0.0f,
			Animation.RELATIVE_TO_PARENT,  0.0f, Animation.RELATIVE_TO_PARENT,  1.0f
			);
	outtoLeft.setDuration(500);
	outtoLeft.setInterpolator(new AccelerateInterpolator());
	return outtoLeft;
} 

///////////---In from Down, out from Up---//////////////////////
	public static Animation inFromDownAnimation() {
		Animation inFromRight = new TranslateAnimation(
				///X coordinator
				Animation.RELATIVE_TO_PARENT,  0.0f, Animation.RELATIVE_TO_PARENT,  0.0f,
				// Y coodinator
				Animation.RELATIVE_TO_PARENT,  1.0f, Animation.RELATIVE_TO_PARENT,   0.0f
				);
		inFromRight.setDuration(500);
		inFromRight.setInterpolator(new AccelerateInterpolator());
		return inFromRight;
	}
	public static Animation outToUpAnimation() {
		Animation outtoLeft = new TranslateAnimation(
				Animation.RELATIVE_TO_PARENT,  0.0f, Animation.RELATIVE_TO_PARENT,  0.0f,
				Animation.RELATIVE_TO_PARENT,  0.0f, Animation.RELATIVE_TO_PARENT,   -1.0f
				);
		outtoLeft.setDuration(500);
		outtoLeft.setInterpolator(new AccelerateInterpolator());
		return outtoLeft;
	} 

}
