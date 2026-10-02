import os
import subprocess
import time

project_dir = r"C:\Users\USER\Pertemuan3_263"
file_path = os.path.join(project_dir, r"app\src\main\java\com\example\pertemuan3_263\Tataletak.kt")

def run_git(args):
    result = subprocess.run(["git"] + args, cwd=project_dir, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Git error: {result.stderr}")
    return result

# 1. Initialize git if not already
run_git(["init"])
# Configure dummy user just in case
run_git(["config", "user.name", "Andhikaryanstito"])
run_git(["config", "user.email", "praktikum@kampus.ac.id"])

# 2. Back up original file to read it later if needed, though we will rewrite it
with open(file_path, "r", encoding="utf-8") as f:
    original_content = f.read()

with open(file_path + ".bak", "w", encoding="utf-8") as f:
    f.write(original_content)

# 3. Create initial commit with everything EXCEPT Tataletak.kt changes (we clear Tataletak.kt first)
with open(file_path, "w", encoding="utf-8") as f:
    f.write("package com.example.pertemuan3_263\n")

run_git(["add", "."])
run_git(["commit", "-m", "Initial commit: Setup project and resources"])

# 4. Now apply the 15 steps
blocks = [
    ("Add basic layout imports", """package com.example.pertemuan3_263

import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
"""),
    
    ("Create TataletakColumn layout", """
@Composable
fun TataletakColumn(modifier: Modifier = Modifier) {
    Column(
        modifier = modifier.padding(top = 20.dp, start = 20.dp, end = 20.dp)
    ) {
        Text(text = "Komponen 1")
        Text(text = "Komponen 2")
        Text(text = "Komponen 3")
        Text(text = "Komponen 4")
    }
}
"""),
    
    ("Create TataletakRow layout", """
@Composable
fun TataletakRow(modifier: Modifier = Modifier) {
    Row(
        modifier = modifier.fillMaxWidth(),
        horizontalArrangement = Arrangement.SpaceEvenly
    ) {
        Text(text = "Komponen 1")
        Text(text = "Komponen 2")
        Text(text = "Komponen 3")
        Text(text = "Komponen 4")
    }
}
"""),

    ("Create TataletakBox layout", """
@Composable
fun TataletakBox(modifier: Modifier = Modifier) {
    Box(
        modifier = modifier
            .fillMaxHeight()
            .fillMaxWidth(),
        contentAlignment = Alignment.Center
    ) {
        Text(text = "Box 1")
        Text(text = "Column 1")
        Text(text = "Row 1")
        Text(text = "Box 2")
        Text(text = "Column 2")
    }
}
"""),

    ("Create TataletakColumnRow combination", """
@Composable
fun TataletakColumnRow(modifier: Modifier = Modifier) {
    Column(modifier = modifier) {
        // Baris 1
        Row(
            modifier = Modifier.fillMaxWidth(),
            horizontalArrangement = Arrangement.SpaceEvenly
        ) {
            Text(text = "Komponen 1 Baris 1")
            Text(text = "Komponen 2 Baris 1")
            Text(text = "Komponen 3 Baris 1")
        }
        // Baris 2
        Row(
            modifier = Modifier.fillMaxWidth(),
            horizontalArrangement = Arrangement.SpaceEvenly
        ) {
            Text(text = "Komponen 1 Baris 2")
            Text(text = "Komponen 2 Baris 2")
            Text(text = "Komponen 3 Baris 2")
        }
    }
}
"""),

    ("Create TataletakRowColumn combination", """
@Composable
fun TataletakRowColumn(modifier: Modifier = Modifier) {
    Row(
        modifier = modifier.fillMaxWidth(),
        horizontalArrangement = Arrangement.SpaceEvenly
    ) {
        Column {
            Text(text = "Komponen 1 Kolom 1")
            Text(text = "Komponen 2 Kolom 1")
            Text(text = "Komponen 3 Kolom 1")
        }
        Column {
            Text(text = "Komponen 1 Kolom 2")
            Text(text = "Komponen 2 Kolom 2")
            Text(text = "Komponen 3 Kolom 2")
        }
    }
}
"""),
    
    ("Start TataletakBoxColumnRow and load image resource", """
@Composable
fun TataletakBoxColumnRow(modifier: Modifier = Modifier) {
    val gambar = painterResource(id = R.drawable.notasinatom)

    Column(modifier = modifier.fillMaxSize()) {
"""),
    
    ("Add yellow Box for header in TataletakBoxColumnRow", """
        Box(
            modifier = Modifier
                .fillMaxWidth()
                .height(110.dp)
                .background(color = Color.Yellow),
            contentAlignment = Alignment.Center
        ) {
            Column {
"""),

    ("Add first Row for header data", """
                Row(
                    modifier = Modifier.fillMaxWidth(),
                    horizontalArrangement = Arrangement.SpaceEvenly
                ) {
                    Text(text = "Col 1 Row 1 Komponen 1", modifier = Modifier.weight(1f), textAlign = TextAlign.Center)
                    Text(text = "Col 1 Row 1 Komponen 2", modifier = Modifier.weight(1f), textAlign = TextAlign.Center)
                    Text(text = "Col 1 Row 1 Komponen 3", modifier = Modifier.weight(1f), textAlign = TextAlign.Center)
                }
"""),

    ("Add second Row for header data and close header Box", """
                Row(
                    modifier = Modifier.fillMaxWidth(),
                    horizontalArrangement = Arrangement.SpaceEvenly
                ) {
                    Text(text = "Col 1 Row 2 Komponen 1", modifier = Modifier.weight(1f), textAlign = TextAlign.Center)
                    Text(text = "Col 1 Row 2 Komponen 2", modifier = Modifier.weight(1f), textAlign = TextAlign.Center)
                    Text(text = "Col 1 Row 2 Komponen 3", modifier = Modifier.weight(1f), textAlign = TextAlign.Center)
                }
            }
        }
"""),

    ("Add Spacer separating header and content", """
        Spacer(modifier = Modifier.height(10.dp))
"""),

    ("Add cyan Box for content area", """
        Box(
            modifier = Modifier
                .fillMaxWidth()
                .height(300.dp)
                .background(color = Color.Cyan),
            contentAlignment = Alignment.Center
        ) {
"""),

    ("Add background image to content Box", """
            Image(
                painter = gambar,
                contentDescription = null,
                contentScale = ContentScale.Fit
            )
"""),

    ("Add layout title text to content Box and close blocks", """
            Text(
                text = "My Layout",
                fontSize = 50.sp,
                color = Color.Red,
                fontWeight = FontWeight.Bold,
                fontFamily = FontFamily.Cursive,
                modifier = Modifier.align(Alignment.Center)
            )
        }
    }
}
"""),

    ("Add Preview for TataletakBoxColumnRow", """
@Preview(showBackground = true)
@Composable
fun TataletakPreview() {
    TataletakBoxColumnRow()
}
""")
]

current_content = ""
for commit_msg, block in blocks:
    if current_content == "":
        current_content = block
    else:
        current_content += block
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(current_content)
    
    run_git(["add", file_path])
    run_git(["commit", "-m", commit_msg])

print(run_git(["log", "--oneline", "-n", "20"]).stdout)
