from qiskit import *

def kekka (key : str) -> bool:
    def calc ():
        # Use Aer's qasm_simulator
        backend = BasicAer.get_backend('statevector_simulator')

        # Create a Quantum Circuit acting on the q register
        circuit = QuantumCircuit(2, 2)

        circuit.x(0)

        # Add a H gate on qubit 0
        if key == "h":
            print("your input is hgate")
            circuit.h(0)
        elif key == "x":
            print("yout input is xgate")
            circuit.x(0)
        elif key == "cx":
            print("your input is cxgate")
            circuit.cx(0,1)
        else :
            print("your input is unacceptable gate")
            return

        # Map the quantum measurement to the classical bits
        # circuit.measure(0,0)

        # Execute the circuit on the qasm simulator
        job = execute(circuit, backend)

        # Grab results from the job
        result = job.result()

        # Returns counts
        outputstate = result.get_statevector(circuit, decimals=3)
        print("\nTotal count for 00 and 11 are:",outputstate)

        return outputstate

    def isTrue(outputstate):
        state0 = (0+0.j)
        state1 = (1+0.j)
        if len(outputstate) == 4 :
            if outputstate[0] == state0 and outputstate[1] == state0 and outputstate[2] == state0 and outputstate[3] == state1:
                print("Your answer is correct!!")
                return True
            else :
                print("Your answer is uncorrect!!")
                print(outputstate[1])
                return False
        else :
            print("length of outputstate is no correct!!")
            return False


    return isTrue(calc())
