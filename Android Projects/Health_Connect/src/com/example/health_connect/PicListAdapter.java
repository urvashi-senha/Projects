package com.example.health_connect;

import java.util.ArrayList;
import java.util.List;

import android.content.Context;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.TextView;

public class PicListAdapter extends BaseAdapter {
	private Context mContext;
	private LayoutInflater mInflater;
	private ArrayList<Picture> picList = new ArrayList<Picture>();
	private ArrayList<Picture> listpicOrigin = new ArrayList<Picture>();

	public PicListAdapter(Context context, ArrayList<Picture> picList) {
		Log.d("Error","adapter ok");
		mContext = context;
		this.picList = picList;
		Log.d("piclist added : ",  picList.get(0).getPicName());
		Log.d("piclist added : ",  picList.get(1).getPicName());
		
		mInflater = LayoutInflater.from(mContext);
		this.listpicOrigin = new ArrayList<Picture>();
		this.listpicOrigin.addAll(picList);
		Log.d("Error","piclistorigin");
	}

	public class ViewHolder {
		TextView picName;
		TextView picType;
		ImageView picIcon;
	}

	public View getView(int position, View view, ViewGroup parent) {
		final ViewHolder holder;
		if (view == null) {
			Log.d("Error","in get view");
			holder = new ViewHolder();
			Log.d("Error","holder added");
			view = mInflater.inflate(R.layout.list_item, null);
			holder.picName = (TextView) view.findViewById(R.id.pic_name_txt);
			holder.picType = (TextView) view.findViewById(R.id.pic_type_txt);
			holder.picIcon = (ImageView) view.findViewById(R.id.pic_icon_img);
			Log.d("Error","holder view");
			view.setTag(holder);
			Log.d("Error","views found");
		} else {
			holder = (ViewHolder) view.getTag();
		}

		holder.picName.setText(picList.get(position).getPicName());
		holder.picType.setText(picList.get(position).getPicType());
		holder.picIcon.setImageResource(picList.get(position).getPicSource());
		Log.d("Error","info added");
		return view;
	}

	public int getCount() {
		return picList.size();
	}

	public Picture getItem(int position) {
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
	public void filter(String charText) {
		charText = charText.toLowerCase();
		picList.clear();
		if (charText.length() == 0) {
			picList.addAll(listpicOrigin);
		} else {
			for (Picture pic : listpicOrigin) {
				if (pic.getPicName().toLowerCase().contains(charText)) {
					picList.add(pic);
				}
			}
		}
		notifyDataSetChanged();
	}

}