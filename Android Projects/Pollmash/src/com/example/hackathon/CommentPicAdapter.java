package com.example.hackathon;

import java.util.ArrayList;
import java.util.List;



import android.os.Bundle;
import android.app.Activity;
import android.content.Context;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.Menu;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.TextView;

public class CommentPicAdapter extends BaseAdapter {
	private Context mContext;
	private LayoutInflater mInflater;
	private List<Comments> picList = null;
	private ArrayList<Comments> listpicOrigin;

	public CommentPicAdapter(Context context, List<Comments> picList) {
		mContext = context;
		this.picList = picList;
		mInflater = LayoutInflater.from(mContext);
		this.listpicOrigin = new ArrayList<Comments>();
		this.listpicOrigin.addAll(picList);
		Log.d("Error","piclistorigin added");
	}

	public class ViewHolder {
		
		TextView picName;
		TextView picBy;
	}

	public View getView(int position, View view, ViewGroup parent) {
		Log.d("Error","here1");
		final ViewHolder holder;
		if (view == null) {
			Log.d("Error","here21");
			holder = new ViewHolder();
			view = mInflater.inflate(R.layout.list_item2, null);
			holder.picName = (TextView) view.findViewById(R.id.pic_name_txt);
			Log.d("Error","here22");
			holder.picBy = (TextView) view.findViewById(R.id.pic_by_txt);
			Log.d("Error","here23");
			
			view.setTag(holder);
		} else {
			Log.d("Error","here3");
			holder = (ViewHolder) view.getTag();
		}
		Log.d("Error","here4");
		holder.picName.setText(picList.get(position).getPicName());
	
		holder.picBy.setText(picList.get(position).getPicBy());
		Log.d("Error","here5");
		return view;
	}

	public int getCount() {
		return picList.size();
	}

	public Comments getItem(int position) {
		return picList.get(position);
	}

	public long getItemId(int position) {
		return position;
	}

	/**
	 * Filter
	 * @author 9Android.net
	 * 
	 */
	

}