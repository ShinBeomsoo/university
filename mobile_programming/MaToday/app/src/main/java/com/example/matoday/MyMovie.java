package com.example.matoday;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Spinner;

public class MyMovie extends Activity {
    Spinner spinner;
    @Override
    protected void onCreate(Bundle savedInstance) {
        super.onCreate(savedInstance);
        setContentView(R.layout.my_movie);

        spinner = findViewById(R.id.movie_spinner);
        ArrayAdapter spinnerAdapter = ArrayAdapter.createFromResource(
                this, R.array.spinner, android.R.layout.simple_spinner_dropdown_item
        );
        spinnerAdapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinner.setAdapter(spinnerAdapter);
        spinner.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> adapterView, View view, int position, long l) {
                System.out.println(position);
                Intent movieIntent = getIntent();
                int screenNumber = movieIntent.getIntExtra("화면", 0);
                final Intent intent;
                if (position != screenNumber) {
                    switch (position) {
                        case 0:
                            intent = new Intent(getApplicationContext(), MainActivity.class);
                            intent.putExtra("화면", 0);
                            startActivity(intent);
                            break;
                        case 2:
                            intent = new Intent(getApplicationContext(), MyBook.class);
                            intent.putExtra("화면", 0);
                            startActivity(intent);
                            break;
                        default:
                            break;
                    }
                }
            }

            @Override
            public void onNothingSelected(AdapterView<?> adapterView) {
                System.out.println("아무것도 선택된 것이 없습니다.");
            }
        });
    }
}
