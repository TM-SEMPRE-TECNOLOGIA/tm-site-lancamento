import cv2
import os

def extract(video_path, output_dir, target_frames=150):
    os.makedirs(output_dir, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    total_video_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    duration = total_video_frames / fps if fps > 0 else 10
    
    print(f"Vídeo: {video_path}")
    print(f"Total de frames no vídeo original: {total_video_frames} ({fps:.1f} fps, {duration:.1f}s)")
    print(f"Extraindo {target_frames} quadros em Full HD com alta qualidade...")

    step = total_video_frames / target_frames
    extracted = 0

    for i in range(target_frames):
        frame_idx = int(i * step)
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
        ret, frame = cap.read()
        if not ret:
            break
        
        # Salva em JPG com 90% de qualidade (nítido e super rápido para carregar)
        out_path = os.path.join(output_dir, f"frame_{i:03d}.jpg")
        cv2.imwrite(out_path, frame, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
        extracted += 1

    cap.release()
    print(f"Concluído! {extracted} frames salvos em '{output_dir}'.")

if __name__ == '__main__':
    extract("assets-video-cover.mp4", "frames", target_frames=150)
