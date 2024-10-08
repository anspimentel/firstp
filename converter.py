from moviepy.editor import VideoFileClip

def convert_mod_to_mp4(input_file, output_file):
    try:
        clip = VideoFileClip(input_file)
        clip.write_videofile(output_file, codec="libx264")
        print(f"Conversion successful: {output_file}")
    except Exception as e:
        print(f"Error during conversion: {str(e)}")

# Exemplo de uso
input_file = "video.mod"  # Nome do arquivo de entrada
output_file = "video.mp4"  # Nome do arquivo de saída

convert_mod_to_mp4(input_file, output_file)
