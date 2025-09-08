# Criar a classe Main

class Computador:
    def __init__(self, marca, modelo, gpu_nome, gpu_memoria, cpu_nome, cpu_cores, cpu_clock):
        self.marca = marca
        self.modelo = modelo
        self.gpu = self.GPU(gpu_nome, gpu_memoria)
        self.cpu = self.CPU(cpu_nome, cpu_cores, cpu_clock)

    def mostrar_configuracao(self):
        print(f'Computador: {self.modelo}')
        self.gpu.mostrar_gpu()
        self.cpu.mostrar_cpu()

    class GPU:
        def __init__(self, nome, memoria_gb):
            self.nome = nome
            self.memoria_gb = memoria_gb

        def mostrar_gpu(self):
            print(f'GPU: {self.nome}, Memória: {self.memoria_gb} GB')

    class CPU:
        def __init__(self, nome, cores, clock_ghz):
            self.nome = nome
            self.cores = cores
            self.clock_ghz = clock_ghz

        def mostrar_cpu(self):
            print(f'CPU: {self.nome}, Cores: {self.cores}, Clock: {self.clock_ghz} GHz')

# Utilização
pc1 = Computador("Dell", "Inspiron", "NVIDIA GTX 1660", 6, "Intel i7", 8, 3.6)
pc1.mostrar_configuracao()

print()

pc2 = Computador("HP", "Pavilion", "NVIDIA RTX 3060", 12, "AMD Ryzen 7", 8, 4.0)
pc2.mostrar_configuracao()