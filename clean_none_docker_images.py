import subprocess


def delete_none_docker_images():
    output: bytes = subprocess.check_output('docker images --format="repository={{.Repository}} id={{.ID}}"', shell=True)

    string_output = output.decode("utf-8")
    output_lines: list = string_output.splitlines()

    none_image_id: str = ""
    for image in output_lines:
        if "repository=<none>" in image:
            none_image_id = image.split("id=",1)[1]

    remove_results: bytes = subprocess.check_output(f"docker rmi {none_image_id}", shell=True)
    print(remove_results)


if __name__ == '__main__':
    delete_none_docker_images()
