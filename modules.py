import argparse


def run(occt_path: str, output_path: str):
    # occt_path = "E:/Repos/OCCT-7_6_3/"
    modules_file = occt_path+"/"+"adm/MODULES"

    modules = []
    with open(modules_file, encoding='utf-8') as file:
        for module in file.read().splitlines():
            modules.append(module.split())

    modules.pop()  # 不要最后的tools
    # print(modules)
    packages = {}
    for module in modules:
        for package in module[1:]:
            filename = f'{occt_path}/src/{package}/PACKAGES'
            with open(filename, encoding='utf-8') as file:
                # print(file.read().splitlines())
                packages[package] = file.read().splitlines()

    results = []
    for module in modules:
        v = ' '.join(module)
        results.append(f'set({v})\n')

    for k, v in packages.items():
        result = ' '.join(v)
        results.append(f'set({k} {result})')

    with open(f'{output_path}/modules.cmake',
              mode='w', encoding='utf-8') as file:
        # file.writelines(results)
        file.write('\n'.join(results))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-S", "--OcctSourceDir", type=str, help="OCCT源码根目录")
    parser.add_argument("-O", "--OutputDir", type=str,
                        help="生成的modules.cmake所在路径")
    args = parser.parse_args()

    run(args.OcctSourceDir, args.OutputDir)
