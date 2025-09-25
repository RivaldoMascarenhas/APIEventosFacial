import insightface
import numpy as np
import cv2

_model = None

def get_model():
    global _model
    if _model is None:
        _model = insightface.app.FaceAnalysis(
            name="buffalo_l",
            providers=["CPUExecutionProvider"]
        )
        # Inicializamos com um det_size padrão
        _model.prepare(ctx_id=0, det_size=(640, 640))
    return _model


def generate_embedding(image_path: str) -> np.ndarray:
    """
    Gera embedding facial de uma imagem, ajustando det_size dinamicamente.
    """
    model = get_model()

    # Carrega imagem
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Não foi possível abrir a imagem: {image_path}")

    # Ajusta det_size baseado no tamanho da imagem
    height, width = img.shape[:2]
    max_side = max(height, width)

    # Definimos det_size proporcional
    if max_side <= 640:
        det_size = (320, 320)
    elif max_side <= 1280:
        det_size = (640, 640)
    else:
        det_size = (800, 800)

    # Re-prepara o modelo se det_size mudou
    if model.det_size != det_size:
        model.prepare(ctx_id=0, det_size=det_size)

    # Detecta rostos
    faces = model.get(img)
    if not faces:
        raise ValueError("Nenhum rosto encontrado na imagem.")

    # Pega o primeiro rosto detectado
    face = faces[0]

    return face.embedding.tolist()
