import os
import shutil

def train_dummy(dataset_path="dataset/eliseo", epochs=5):
    print(f"📁 Simulando entrenamiento con datos desde: {dataset_path}")
    for epoch in range(1, epochs+1):
        print(f"🔁 Epoch {epoch}/{epochs}... (simulado)")
    print("✅ Entrenamiento finalizado. Modelo guardado en logs/eliseo/G_100.pth")

if __name__ == "__main__":
    os.makedirs("logs/eliseo", exist_ok=True)
    train_dummy()
    with open("logs/eliseo/G_100.pth", "w") as f:
        f.write("modelo_entrenado_simulado")
