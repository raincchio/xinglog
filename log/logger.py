import os

class Logger:

    def __init__(self, path, task_name, datafile_name, headline):
        '''
        headline: ['eval_reward', 'policy_loss', 'value_loss']
        '''
        # Ensure the directory exists
        data_dir = os.path.join(path, task_name)
        os.makedirs(data_dir, exist_ok=True)

        # Create the log file for writing
        self.writer = open(os.path.join(data_dir, datafile_name), 'w')

        # Prepare log content headers
        log_content = ",".join(headline)
        
        self.content_len =len(headline)
        # Write headers to the log file
        self.writer.write(log_content + '\n')

    def log(self, variable_value):
        '''
        Write a log entry to the file.
        variable_value: [0.1,0.2,0.3]
        '''
        assert len(variable_value)==self.content_len

        log_content = ",".join(map(str, variable_value))
            
        self.writer.write(str(log_content) + '\n')
 

    def close(self):
        '''Close the log file.'''
        if not self.writer.closed:
            self.writer.close()
