package com.example.mytraining;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.CompoundButton;

import java.sql.BatchUpdateException;

public class MainActivity extends AppCompatActivity {
    CheckBox isEnabled;
    CheckBox isClickable;
    CheckBox rotate45;
    Button button;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        isEnabled = (CheckBox) findViewById(R.id.is_enabled);
        isClickable = (CheckBox) findViewById(R.id.is_clickable);
        rotate45 = (CheckBox) findViewById(R.id.rotate_45);
        button = (Button) findViewById(R.id.button);

        isEnabled.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton compoundButton, boolean b) {
                if (isEnabled.isChecked()) {
                    button.setEnabled(false);
                } else {
                    button.setEnabled(true);
                }
            }
        });
        isClickable.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton compoundButton, boolean b) {
                if (isClickable.isChecked()) {
                    button.setClickable(false);
                } else {
                    button.setClickable(true);
                }
            }
        });
        rotate45.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton compoundButton, boolean b) {
                if (rotate45.isChecked()) {
                    button.setRotation(45);
                } else {
                    button.setRotation(0);
                }
            }
        });
    }
}