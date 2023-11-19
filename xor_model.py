from neural_net import *


def test_xor():
    network = Network()
    network.add(FullyConnected(2, 3))
    network.add(Activation(3, sigmoid, sigmoid_derivative))
    network.add(FullyConnected(3, 1))
    network.add(Activation(1, sigmoid, sigmoid_derivative))

    config = TrainingConfig(
        loss=mean_squared_error,
        loss_derivative=mean_squared_error_derivative,
        epochs=1_000,
        learning_rate=0.5)

    labeled_examples = [
        ((0, 0), (0,)),
        ((0, 1), (1,)),
        ((1, 0), (1,)),
        ((1, 1), (0,)),
    ]

    train(network, config, labeled_examples)

    test_examples = labeled_examples

    error_sum = 0
    error_count = 0

    for input_vector, expected_output in test_examples:
        output = predict(network, input_vector)
        print(f'Input={input_vector}, Output={output}')

        mse = config.loss(expected_output, output)
        error_sum += mse
        error_count += 1

    print(f'AvgError={error_sum/error_count:.10f}')


test_xor()