import os
import subprocess

project_dir = r"C:\Users\USER\Pertemuan3_263"
file_path = os.path.join(project_dir, r"app\src\main\java\com\example\pertemuan3_263\TugasLogin.kt")
main_activity_path = os.path.join(project_dir, r"app\src\main\java\com\example\pertemuan3_263\MainActivity.kt")

def run_git(args):
    result = subprocess.run(["git"] + args, cwd=project_dir, capture_output=True, text=True)
    return result

# 1. Commit the newly added images first
run_git(["add", r"app\src\main\res\drawable\admisiumy.jpg"])
run_git(["add", r"app\src\main\res\drawable\masjid.jpg"])
run_git(["commit", "-m", "Tugas Praktikum: Add background and profile images"])

blocks = [
    ("Tugas Praktikum: Add basic structure for Login Screen", """package com.example.pertemuan3_263

import androidx.compose.foundation.Image
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

@Composable
fun TugasLogin() {
"""),

    ("Tugas Praktikum: Add root Box layout", """    Box(modifier = Modifier.fillMaxSize()) {
"""),

    ("Tugas Praktikum: Add full screen background image", """        // Background
        Image(
            painter = painterResource(id = R.drawable.admisiumy),
            contentDescription = "Background",
            contentScale = ContentScale.Crop,
            modifier = Modifier.fillMaxSize()
        )
"""),

    ("Tugas Praktikum: Add Column for centering contents", """        // Content
        Column(
            modifier = Modifier.fillMaxSize(),
            horizontalAlignment = Alignment.CenterHorizontally
        ) {
            Spacer(modifier = Modifier.height(70.dp))
"""),

    ("Tugas Praktikum: Add Login title and subtitle", """            Text(
                text = "Login",
                fontSize = 40.sp,
                fontWeight = FontWeight.Bold,
                color = Color.Blue
            )
            Text(
                text = "Ini adalah halaman login,",
                fontSize = 16.sp,
                color = Color.White
            )
            Spacer(modifier = Modifier.height(30.dp))
"""),

    ("Tugas Praktikum: Add UMY logo in the center", """            Image(
                painter = painterResource(id = R.drawable.notasinatom),
                contentDescription = "Logo UMY",
                modifier = Modifier.size(150.dp)
            )
            Spacer(modifier = Modifier.height(50.dp))
"""),

    ("Tugas Praktikum: Add Name label", """            Text(
                text = "Nama",
                fontSize = 18.sp,
                fontWeight = FontWeight.Bold,
                color = Color.Red
            )
"""),

    ("Tugas Praktikum: Add Student Name", """            Text(
                text = "Andhika Ryan Stito",
                fontSize = 20.sp,
                fontWeight = FontWeight.Bold,
                color = Color.Blue
            )
"""),

    ("Tugas Praktikum: Add Student NIM", """            Text(
                text = "20240140263",
                fontSize = 24.sp,
                fontWeight = FontWeight.Bold,
                color = Color.Black
            )
            Spacer(modifier = Modifier.height(40.dp))
"""),

    ("Tugas Praktikum: Add circular bottom photo", """            Image(
                painter = painterResource(id = R.drawable.masjid),
                contentDescription = "Foto Profil Bawah",
                contentScale = ContentScale.Crop,
                modifier = Modifier
                    .size(200.dp)
                    .clip(CircleShape)
            )
        }
    }
}

@Preview(showBackground = true)
@Composable
fun TugasLoginPreview() {
    TugasLogin()
}
""")
]

current_content = ""
for commit_msg, block in blocks:
    current_content += block
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(current_content)
    
    run_git(["add", file_path])
    run_git(["commit", "-m", commit_msg])

# Finally, change MainActivity.kt to point to TugasLogin()
with open(main_activity_path, "r", encoding="utf-8") as f:
    main_code = f.read()

main_code = main_code.replace("TataletakBoxColumnRow(", "TugasLogin(")

with open(main_activity_path, "w", encoding="utf-8") as f:
    f.write(main_code)

run_git(["add", main_activity_path])
run_git(["commit", "-m", "Tugas Praktikum: Update MainActivity to display Login Screen"])

run_git(["push", "origin", "main"])
